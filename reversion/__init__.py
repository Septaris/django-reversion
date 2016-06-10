"""
An extension to the Django web framework that provides version control for model instances.

Developed by Dave Hall.

<http://www.etianen.com/>
"""

try:
    import django  # noqa
except ImportError:  # pragma: no cover
    # The top-level API requires Django, which might not be present if setup.py
    # is importing reversion to get __version__.
    pass
else:
    from reversion.errors import (  # noqa
        RevertError,
        RevisionManagementError,
        RegistrationError,
    )
    from reversion.revisions import (  # noqa
        # Revision context manager.
        is_active,
        is_manage_manually,
        get_user,
        set_user,
        get_comment,
        set_comment,
        get_date_created,
        set_date_created,
        add_meta,
        add_to_revision,
        create_revision,
        # Revision manager.
        RevisionManager,
        default_revision_manager,
        register,
        is_registered,
        unregister,
        get_registered_models,
        get_for_model,
        get_for_object_reference,
        get_for_object,
        get_deleted,

    )

__version__ = VERSION = (1, 10, 3)
