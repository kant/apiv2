import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from breathecode.authenticate.signals import invite_accepted
from breathecode.authenticate.models import ProfileAcademy
from breathecode.admissions.models import CohortUser, Cohort
from breathecode.events.models import Event
from .models import Downloadable
from breathecode.events.signals import event_saved
from .signals import downloadable_saved
from breathecode.admissions.signals import student_edu_status_updated, cohort_saved
from .models import FormEntry, ActiveCampaignAcademy
from .tasks import add_cohort_task_to_student, add_cohort_slug_as_acp_tag, add_event_slug_as_acp_tag, add_downloadable_slug_as_acp_tag

logger = logging.getLogger(__name__)


@receiver(invite_accepted, sender=ProfileAcademy)
def post_save_profileacademy(sender, instance, **kwargs):
    # if a new ProfileAcademy is created on the authanticate app
    # look for the email on the formentry list and bind it
    logger.debug(
        'Receiver for invite_accepted triggered, linking the new user to its respective form entries')
    entries = FormEntry.objects.filter(email=instance.user.email, user__isnull=True)
    for entry in entries:
        entry.user = instance.user
        entry.save()


@receiver(student_edu_status_updated, sender=CohortUser)
def student_edustatus_updated(sender, instance, *args, **kwargs):
    if instance.educational_status == 'ACTIVE':
        logger.warn(f'Student is now active in cohort `{instance.cohort.slug}`, processing task')
        add_cohort_task_to_student.delay(instance.user.id, instance.cohort.id, instance.cohort.academy.id)


@receiver(cohort_saved, sender=Cohort)
def cohort_post_save(sender, instance, created, *args, **kwargs):
    if created:
        ac_academy = ActiveCampaignAcademy.objects.filter(academy__id=instance.academy.id).first()
        if ac_academy is not None:
            add_cohort_slug_as_acp_tag.delay(instance.id, instance.academy.id)


@receiver(event_saved, sender=Event)
def event_save(sender, instance, *args, **kwargs):
    ac_academy = ActiveCampaignAcademy.objects.filter(academy__id=instance.academy.id).first()
    if ac_academy is not None:
        add_event_slug_as_acp_tag.delay(instance.id, instance.academy.id)


@receiver(downloadable_saved, sender=Downloadable)
def downloadable_post_save(sender, instance, created, *args, **kwargs):
    if created:
        ac_academy = ActiveCampaignAcademy.objects.filter(academy__id=instance.academy.id).first()
        if ac_academy is not None:
            add_downloadable_slug_as_acp_tag.delay(instance.id, instance.academy.id)
