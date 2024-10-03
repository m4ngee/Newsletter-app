from django.core.mail import send_mail
from django.utils import timezone
from ...models import Sub, Newsletter, SentNewsletter

def send_newsletter(newsletter_id):
    try:
        newsletter = Newsletter.objects.get(id=newsletter_id)
        subs = Sub.objects.filter(active=True)

        for sub in subs:
            try:
                send_mail(
                    subject=newsletter.subject,
                    message=newsletter.body,
                    from_email='newsletter@mangodev.cloud',
                    recipient_list=[sub.email],
                    fail_silently=False,
                )
                
                SentNewsletter.objects.create(
                    newsletter=newsletter,
                    sub=sub,
                    sent_on=timezone.now(),
                    status='sent'
                )

            except Exception as e:

                SentNewsletter.objects.create(
                    newsletter=newsletter,
                    sub=sub,
                    sent_on=timezone.now(),
                    status='failed'
                )
        
        newsletter.was_sent = True
        newsletter.sent_on = timezone.now()
        newsletter.save()
    
    except Newsletter.DoesNotExist:
        print(f'Newsletter {newsletter_id} does not exist')

