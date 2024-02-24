
# st-tiny-editor

st-tiny-editor is a versatile Streamlit component designed to enhance your application's text editing capabilities. With st-tiny-editor, you can effortlessly integrate the robust TinyMCE editor into your Streamlit applications, providing users with a seamless and intuitive editing experience.

TinyMCE is a feature-rich WYSIWYG editor that offers a plethora of customization options, making it ideal for various text editing tasks. Whether you're building a blog, a content management system, or simply need a more interactive text input for your Streamlit app, st-tiny-editor has you covered.

With st-tiny-editor, you can:

- **Enable Rich Text Editing**: Allow users to format text with a variety of styles, fonts, colors, and more.
- **Insert Images and Media**: Easily insert images and media files into the editor to enrich content.
- **Customize Toolbar and Plugins**: Tailor the editor's toolbar and enable/disable plugins to suit your application's specific needs.
- **Control Editor Height and Styling**: Adjust the editor's height and apply custom CSS styles to seamlessly integrate with your app's design.

Enhance your Streamlit applications with st-tiny-editor and empower your users with an intuitive and feature-rich text editing experience.

## Installation

You can install `st-tiny-editor` via pip:

```bash
pip install st-tiny-editor
```

## Usage

The `tiny_editor` function initializes a text editor with specified parameters and default values if not provided.

### Parameters

- **apiKey** (str, optional): Specifies an API key for authentication. If no `apiKey` is provided, the editor will be disabled.
- **initialValue** (str, optional): Specifies the initial content to be displayed in the editor. Defaults to an empty string if not provided.
- **key** (str, optional): Specifies a unique identifier for the editor instance. Useful when working with multiple editor instances on the same page.
- **height** (int, optional): Specifies the height of the editor in pixels. Defaults to 200 if not provided.
- **menubar** (bool, optional): Specifies whether the editor should display a menu bar. Defaults to False.
- **plugins** (list of str, optional): Specifies a list of plugins that should be enabled in the editor. Defaults to a standard set of plugins.
- **toolbar** (str, optional): Specifies the toolbar configuration for the editor. Defaults to a standard toolbar configuration.
- **content_style** (str, optional): Specifies the CSS styles that should be applied to the editor content. Defaults to a standard style.
- **disabled** (bool, optional): Specifies whether the editor should be disabled. Defaults to False.

For more information on available options, refer to the [TinyMCE documentation](https://www.tiny.cloud/docs/tinymce/latest/react-ref/).

### Example

Here's an example demonstrating the usage of the `tiny_editor` function:

```python
from st_tiny_editor import tiny_editor
import streamlit as st

# Initialize the TinyMCE editor
editor_content = tiny_editor(
    apiKey=st.secrets["TINY_API_KEY"],
    height=1000,
    initialValue="<p>Hello World</p>",
    toolbar='undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | link image media table | align lineheight | numlist bullist indent outdent | emoticons charmap | removeformat'
)

# Display the content entered in the editor
st.write(editor_content, unsafe_allow_html=True)
```

In this example, we initialize the TinyMCE editor with a specified API key, height, initial content, and custom toolbar configuration. The content entered by the user in the editor is then displayed using Streamlit's `write` function.

## Development

To contribute to `st-tiny-editor`, follow these steps:

1. Clone this repository: `git clone https://github.com/your_username/st-tiny-editor`
2. Navigate to the repository: `cd st-tiny-editor`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Navigate to the `streamlit_tiny_editor` directory: `cd streamlit_tiny_editor`
5. Install Yarn if you haven't already: [Yarn Installation Guide](https://classic.yarnpkg.com/en/docs/install/)
6. Install the frontend dependencies by running `yarn install` in the `frontend` directory.
7. Make changes and test them.
8. Submit a pull request!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io) - For providing an amazing platform for building data apps.
- [TinyMCE](https://www.tiny.cloud/) - For the rich text editing capabilities.

---

Feel free to customize this README to better fit your package's features and requirements.
