import os
from typing import  Optional, Union
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = True

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        "st_tiny_editor",
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_tiny_editor", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def tiny_editor(apiKey: str = None, initialValue: Optional[str] = None, key: Optional[str] = None, **kwargs) -> Union[str, None]:
    """
    The `tiny_editor` function initializes a text editor with specified parameters and default values if not provided.

    :param apiKey: The `apiKey` parameter in the `tiny_editor` function is used to specify an API key for authentication. If
    no `apiKey` is provided when calling the function, the  editor will be initialized with disabled features

    :param initialValue: The `initialValue` parameter in the `tiny_editor` function is used to specify the initial content
    that will be displayed in the editor when it is loaded. If no initial content is provided, the editor will be empty by
    default

    :param key: The `key` parameter in the `tiny_editor` function is used to specify a unique identifier for the editor
    instance. This identifier can be useful when working with multiple editor instances on the same page or when you need to
    differentiate between different instances of the editor

    You can also specify the following optional parameters when calling the `tiny_editor` function:

    :param height: The `height` parameter in the `tiny_editor` function is used to specify the height of the editor in pixels.

    :param menubar: The `menubar` parameter in the `tiny_editor` function is used to specify whether the editor should display

    :param plugins: The `plugins` parameter in the `tiny_editor` function is used to specify a list of plugins that should be enabled

    :param toolbar: The `toolbar` parameter in the `tiny_editor` function is used to specify the toolbar configuration for the editor

    :param content_style: The `content_style` parameter in the `tiny_editor` function is used to specify the CSS styles that should be applied to the editor content

    :param disabled: The `disabled` parameter in the `tiny_editor` function is used to specify whether the editor should be disabled

    for more information visit https://www.tiny.cloud/docs/tinymce/latest/react-ref/

    :return: The function `tiny_editor` is returning the text provided by the user in the editor in html format
    """

    if apiKey is None:
        apiKey = "API_KEY_NOT_PROVIDED"

    if initialValue is None:
        initialValue = ""

    if 'height' not in kwargs:
        kwargs['height'] = 200

    if 'menubar' not in kwargs:
        kwargs['menubar'] = False

    if 'plugins' not in kwargs:
        kwargs['plugins'] = [
            'advlist', 'autolink', 'lists', 'link', 'image', 'charmap', 'preview',
            'anchor', 'searchreplace', 'visualblocks', 'code', 'fullscreen',
            'insertdatetime', 'media', 'table', 'code', 'help', 'wordcount'
          ]
    if 'toolbar' not in kwargs:
        kwargs['toolbar'] = ('undo redo | blocks | ' +
            'bold italic forecolor | alignleft aligncenter ' +
            'alignright alignjustify | bullist numlist outdent indent | ' +
            'link image | code'+ 'removeformat | help')

    if 'content_style' not in kwargs:
        kwargs['content_style'] = 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }'

    if 'disabled' not in kwargs:
        kwargs['disabled'] = False


    component_value = _component_func(apiKey=apiKey, initialValue=initialValue, key=key, **kwargs)


    #write(apiKey, content, key, kwargs)

    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    return component_value
