from setup.models import Setup

from django import template


register = template.Library()
setup = Setup.objects.first()







@register.simple_tag
def name():
    
    return setup.owner.user.first_name + " " +  setup.owner.user.last_name

@register.simple_tag
def test():
    return setup.owner.user.first_name


@register.simple_tag
def avatar():
    return setup.owner.photo.url



@register.simple_tag
def subtitle():
    return setup.subtitle



@register.simple_tag
def photo():
    return setup.mian_photo.url



@register.simple_tag
def description():
    return setup.description


@register.simple_tag
def email():
    return setup.owner.user.email


@register.simple_tag
def phone():
    return setup.owner.phone

# socials

@register.simple_tag
def twitter():
    return setup.twitter



@register.simple_tag
def instagram():
    return setup.instagram



@register.simple_tag
def pinterest():
    return setup.pinterest


@register.simple_tag
def vk():
    return setup.vk


# @register.simple_tag
# def post_list():
#     return setup.vk
