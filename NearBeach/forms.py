from __future__ import unicode_literals
from django import forms
from django.forms import ModelForm

# Import from Models
from .models import *


class AddBugForm(forms.Form):
    bug_client = forms.ModelChoiceField(
        required=True,
        queryset=bug_client.objects.filter(
            is_deleted="FALSE",
        )
    )
    bug_id = forms.IntegerField(
        required=True,
        min_value=0,
    )
    bug_description = forms.CharField(
        required=True,
    )
    bug_status = forms.CharField(
        required=True,
    )


class AddCustomerForm(forms.Form):
    customer = forms.ModelChoiceField(
        required=True,
        queryset=customer.objects.all(),
    )


class AddFolderForm(forms.Form):
    folder_description = forms.CharField(
        required=True,
        max_length=50,
    )
    parent_folder = forms.ModelChoiceField(
        required=False,
        queryset=folder.objects.all(),
    )


class AddGroupForm(forms.Form):
    group_list = forms.ModelMultipleChoiceField(
        required=True,
        queryset=group.objects.all(),
    )


class AddLinkForm(forms.Form):
    document_description = forms.CharField(
        max_length=50,
        required=True,
    )
    document_url_location = forms.URLField(
        required=True,
    )
    parent_folder = forms.ModelChoiceField(
        required=False,
        queryset=folder.objects.all(),
    )


class AddNoteForm(forms.Form):
    note = forms.CharField(
        required=True,
    )


class AddRequirementLinkForm(forms.Form):
    # One external field
    project = forms.ModelMultipleChoiceField(
        required=False,
        queryset=project.objects.filter(
            is_deleted="FALSE",
        )
    )
    task = forms.ModelMultipleChoiceField(
        required=False,
        queryset=task.objects.filter(
            is_deleted="FALSE",
        )
    )
    opportunity = forms.ModelMultipleChoiceField(
        required=False,
        queryset=opportunity.objects.filter(
            is_deleted="FALSE",
        )
    )


class DocumentUploadForm(ModelForm):
    document = forms.FileField(
        required=True,
    )
    parent_folder = forms.ModelChoiceField(
        required=False,
        queryset=folder.objects.all(),
    )

    class Meta:
        model = document
        fields = {
            'document',
            'document_description',
        }


class AddUserForm(forms.Form):
    user_list = forms.ModelMultipleChoiceField(
        required=True,
        queryset=User.objects.all(),
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control',
            'required': True,
            'autofocus': True,
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control',
            'required': True,
        })
    )


class NewOrgnanisationForm(forms.ModelForm):
    # Basic Meta data
    class Meta:
        model = organisation
        fields = [
            'organisation_name',
            'organisation_website',
            'organisation_email',
        ]


class NewRequirementItemForm(forms.ModelForm):
    # Basic Meta data
    class Meta:
        model = requirement_item
        fields = [
            'requirement_item_title',
            'requirement_item_scope',
            'requirement_item_status',
            'requirement_item_type',
        ]


class NewRequirementForm(forms.ModelForm):
    # One external field
    group_list = forms.ModelMultipleChoiceField(
        required=True,
        queryset=group.objects.filter(
            is_deleted="FALSE",
        )
    )

    # Basic Meta data
    class Meta:
        model = requirement
        fields = [
            'requirement_title',
            'requirement_scope',
            'requirement_status',
            'requirement_type',
            'organisation',
        ]


class QueryBugClientForm(forms.Form):
    bug_client_id = forms.ModelChoiceField(
        required=True,
        queryset=bug_client.objects.filter(
            is_deleted="FALSE",
        )
    )
    search = forms.CharField(
        max_length=50,
    )


class SearchForm(forms.Form):
    # Just have a simple search field
    search = forms.CharField(
        required=False,
    )


class UpdateRequirementForm(forms.ModelForm):
    # Basic Meta data
    class Meta:
        model = requirement
        fields = [
            'requirement_title',
            'requirement_scope',
            'requirement_status',
            'requirement_type',
        ]


class UpdateRequirementItemForm(forms.ModelForm):
    # Basic Meta data
    class Meta:
        model = requirement_item
        fields = [
            'requirement_item_title',
            'requirement_item_scope',
            'requirement_item_status',
            'requirement_item_type',
        ]
