from django.contrib import admin
from django.contrib import messages
from .models import Sub
from .models import Newsletter
from.models import SentNewsletter
from mail_app.management.commands.send_newsletter_file import send_newsletter

# Register your models here.

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'was_sent', 'sent_on')

    def send_newsletter_action(self, request, queryset):
        for newsletter in queryset:
            
                try:
                    # Call your sending logic for each newsletter
                    send_newsletter(newsletter.id)
                    self.message_user(request, f'Newsletter "{newsletter.subject}" has been sent.', level=messages.SUCCESS)
                except Exception as e:
                    self.message_user(request, f'Failed to send newsletter "{newsletter.subject}". Error: {e}', level=messages.ERROR)
            
    # Register the action
    actions = [send_newsletter_action]
    send_newsletter_action.short_description = "Send selected newsletters to subscribers"



admin.site.register(Sub)
admin.site.register(Newsletter, NewsletterAdmin)

