from django.views.generic import ListView, DeleteView, UpdateView, CreateView, TemplateView, DetailView
from django.urls import reverse_lazy
from mailing.forms import ClientForm, MailingForm, MessageForm
from mailing.models import Client, Mailing, Message


class ClientListView(ListView):
    model = Client
    template_name = "mailing/client_list.html"


class ClientDetailView(DetailView):
    model = Client
    template_name = "mailing/client_detail.html"


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("mailing:client_list")


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("mailing:client_list")


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("mailing:client_list")


class MailingListView(ListView):
    model = Mailing
    template_name = "mailing/mailing_list.html"


class MailingDetailView(DetailView):
    model = Mailing
    template_name = "mailing/mailing_detail.html"


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:mailing_list")


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:mailing_list")


class MailingDeleteView(DetailView):
    model = Mailing
    success_url = reverse_lazy("mailing:mailing_list")


class MessageListView(ListView):
    model = Message
    template_name = "mailing/message_list.html"


class MessageDetailView(DetailView):
    model = Message
    template_name = "mailing/message_detail.html"


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailing:message_list")


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailing:message_list")


class MessageDeleteView(DetailView):
    model = Message
    success_url = reverse_lazy("mailing:message_list")

