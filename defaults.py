from mezzanine.conf import register_setting

register_setting(
    name='SOUNDCLOUD_URL',
    label='Soundcloud URL',
    description='Full URL for the Soundcloud social media button',
    editable=True,
    default=''
)

register_setting(
    name='YOUTUBE_URL',
    label='Youtube URL',
    description='Full URL for the Youtube social media button',
    editable=True,
    default=''
)

register_setting(
    name='FACEBOOK_URL',
    label='Facebook URL',
    description='Full URL for the Facebook social media button',
    editable=True,
    default=''
)

register_setting(
    name='TWITTER_URL',
    label='Twitter URL',
    description='Full URL for the Twitter social media button',
    editable=True,
    default=''
)
register_setting(
    name='FOOTER_IMG_LOCATION',
    label='Footer Image Location',
    description='Server location of the footer background image (starting in /static/)',
    editable=True,
    default=''
)

# Make the above settings accessible from inside templates
register_setting(
    name='TEMPLATE_ACCESSIBLE_SETTINGS',
    description='Sequence of setting names available within templates.',
    editable=False,
    default=('SOUNDCLOUD_URL', 'FACEBOOK_URL', 'YOUTUBE_URL', 'TWITTER_URL', 'FOOTER_IMG_LOCATION'),
    append=True
)
