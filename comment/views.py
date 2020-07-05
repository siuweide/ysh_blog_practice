from .models import Comment
from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from .forms import CommentForm

def update_comment(request):
    referer = request.META.get('HTTP_REFERER', '/')
    comment_form = CommentForm(request.POST, user=request.user)
    if comment_form.is_valid():
        comment = Comment()
        comment.user = comment_form.cleaned_data['user']
        comment.text = comment_form.cleaned_data['text']
        comment.content_object = comment_form.cleaned_data['content_object']
        comment.save()
        return redirect(referer)
    else:
        return render(request, 'error.html', {'message': comment_form.errors, 'referer_to': referer})
