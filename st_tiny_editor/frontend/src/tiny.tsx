import {
  Streamlit,
  withStreamlitConnection,
  ComponentProps
} from "streamlit-component-lib"
import React, { useRef, useEffect } from 'react';
import { Editor } from '@tinymce/tinymce-react';

function App(props: ComponentProps) {
    const {apiKey, initialValue, height, menubar, plugins, toolbar, content_style,disabled} = props.args;
    useEffect(() => Streamlit.setFrameHeight(height));
    const editorRef = useRef<any>(null);
    return (
      <>
        <Editor
          apiKey={apiKey}
          onInit={(evt, editor) => editorRef.current = editor}
          initialValue={initialValue}
          init={{
            height: height,
            menubar: menubar,
            plugins: plugins,
            toolbar: toolbar,
            content_style: content_style
          }}
          onEditorChange={(value,editor) => Streamlit.setComponentValue(value)}
          disabled={disabled}
        />
      </>
    );
  }


export default withStreamlitConnection(App);
