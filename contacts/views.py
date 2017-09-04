from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.utils.decorators import method_decorator
from django.views.generic.edit import DeleteView

from .models import Contact
from .forms import ContactForm
from .models import Account


@login_required()
def contact_detail(request, uuid):
	account = Account.objects.get(uuid=uuid)
	if account.owner != request.user:
		return HttpResponseForbidden()

	contacts = Contact.objects.filter(account=account)

	variables = {
		'account': account,
		'contacts': contacts
	}

	return render(request,
		'contacts/contact_detail.html', variables
	)


@login_required()
def contact_cru(request, uuid=None, account=None):
	if uuid:
		contact = get_object_or_404(Contact, uuid=uuid)
		if contact.owner != request.user:
			return HttpResponseForbidden()
	else:
		contact = Contact(owner=request.user)

	if request.method == 'POST':
		form = ContactForm(request.POST, instance=contact)
		if form.is_valid():
			account = form.cleaned_data['account']
			if account.owner != request.user:
				return HttpResponseForbidden()
			contact = form.save(commit=False)
			contact.owner = request.user
			contact.save()
			if request.is_ajax():
				return render(request,
							'contacts/contact_item_view.html',
							{'account': account, 'contact': contact}
				)
			else:
				reverse_url = reverse(
					'crmapp.accounts.views.account_detail',
					args=(account.uuid,)
				)
				return HttpResponseRedirect(reverse_url)
		else:
			account = form.cleaned_data['account']
	else:
		form = ContactForm(instance=contact)
	if request.GET.get('account', ''):
		account = Account.objects.get(id=request.GET.get('account', ''))
	variables = {
		'form': form,
		'contact': contact,
		'account': account
	}
	if request.is_ajax():
		template = 'contacts/contact_item_form.html'
	else:
		template = 'contacts/contact_cru.html'
	return render(request, template, variables)


class ContactMixin(object):
	model = Contact

	def get_context_data(self, **kwargs):
		kwargs.update({'object_name': 'Contact'})
		return kwargs

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(ContactMixin, self).dispatch(*args, **kwargs)


class ContactDelete(ContactMixin, DeleteView):
	template_name = 'object_confirm_delete.html'

	def get_object(self, queryset=None):
		obj = super(ContactDelete, self).get_object()
		if not obj.owner == self.request.user:
			raise Http404
		account = Account.objects.get(id=obj.account.id)
		self.account = account
		return obj

	def get_success_url(self):
		return reverse(
			'crmapp.accounts.views.account_detail',
			args=(self.account.uuid,)
		)	









