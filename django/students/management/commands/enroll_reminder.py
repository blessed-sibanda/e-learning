import datetime
from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.mail import send_mass_mail
from django.db.models import Count
from django.contrib.auth.models import User
from django.utils import timezone


class Command(BaseCommand):
    help = 'Sends an e-mail reminder to users registered more ' \
        'than N days that are not yet enrolled into any courses yet'

    def add_arguments(self, parser):
        parser.add_argument('--days', dest='days', type=int)
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        emails = []
        subject = 'Enroll in a course'
        date_joined = timezone.now().today() - \
            datetime.timedelta(days=options['days'])
        users = User.objects.annotate(
            course_count=Count('courses_joined'))  \
            .filter(course_count=0,
                    date_joined__date__lte=date_joined)
        for user in users:
            message = """Dear {},
            
We noticed that you didn't enroll in any courses yet.
What are you waiting for?
            """.format(user.username)
            emails.append(
                (subject, message,
                 'admin@elearning.com',
                 [user.email]))

        send_mass_mail(emails)
        self.stdout.write('Sent {} reminders'.format(len(emails)))
