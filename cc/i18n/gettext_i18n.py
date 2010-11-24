import os
import gettext
import pkg_resources


MO_PATH = pkg_resources.resource_filename(
    'cc.i18n', 'mo')
I18N_DOMAIN = 'cc_org'
CCORG_GETTEXT_TRANSLATIONS = {}


def translations_for_locale(locale, mo_path=MO_PATH):
    """
    Get the right translation and return it
    """
    if CCORG_GETTEXT_TRANSLATIONS.has_key(locale):
        return CCORG_GETTEXT_TRANSLATIONS[locale]

    # do I have the order backwards here?
    langs = [locale]
    if '_' in locale:
        root_lang = locale.split('_')[0]
        if os.path.exists(os.path.join(mo_path, root_lang)):
            langs.append(root_lang)

    if not 'en' in langs:
        langs.append('en')

    translations = gettext.translation(I18N_DOMAIN, mo_path, langs)
    CCORG_GETTEXT_TRANSLATIONS[locale] = translations
    return translations


def ugettext_for_locale(locale, mo_path=MO_PATH):
    def _wrapped_ugettext(message):
        return translations_for_locale(
            locale, mo_path).ugettext(message).decode('utf-8')

    return _wrapped_ugettext
