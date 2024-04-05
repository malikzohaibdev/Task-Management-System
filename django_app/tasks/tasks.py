from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import logging

# Initialize logger
logger = logging.getLogger(__name__)


@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def send_task_notification_email(self, task_id, assigned_user_email):
    try:
        # Log start of the task
        logger.info(f"Sending task notification email for Task ID: {task_id} to {assigned_user_email}")
        from .models import Task
        task = Task.objects.get(id=task_id)
        # Here, implement the logic to fetch task details
        # This is a placeholder for your task fetching logic
        task_title =task.title  # Placeholder title

        # Sending the email
        send_mail(
            subject=f'Notification for Task: {task_title}',
            message=f'A task "{task_title}" has been assigned to you.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[assigned_user_email],
        )

        # Log successful completion
        logger.info(f"Email successfully sent for Task ID: {task_id} to {assigned_user_email}")

    except Exception as e:
        # Log any errors that occur
        logger.error(f"Error sending email for Task ID: {task_id} to {assigned_user_email}: {e}")
        raise
