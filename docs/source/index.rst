html_theme.sidebar_secondary.remove: true

.. template taken from Pandas

.. module:: package_name

package_name documentation
==========================

**Date**: |today| **Version**: |version|


**package_name** 

.. grid:: 1 1 2 2
    :gutter: 2 3 4 4

    .. grid-item-card::
        :img-top: _static/index_user_guide.svg
        :text-align: center

        **User guide**
        ^^^

        The user guide provides in-depth information on the
        key concepts of package_name with useful background information and explanation.

        +++

        .. button-ref:: user_guide
            :color: secondary
            :click-parent:

            To the user guide

    .. grid-item-card::
        :img-top: _static/index_api.svg
        :text-align: center

        **API reference**
        ^^^

        The reference guide contains a detailed description of
        the package_name API. The reference describes how the methods work and which parameters can
        be used. It assumes that you have an understanding of the key concepts.

        +++

        .. button-ref:: quasar-api
            :color: secondary
            :click-parent:

            To the reference guide


.. toctree::
   :maxdepth: 1
   :hidden:

   Installing <#>
   API reference <reference/index>
   Release notes <release>
   User Guide <user_guide/index>