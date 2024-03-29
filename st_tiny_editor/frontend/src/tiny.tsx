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
    const divRef = useRef<HTMLDivElement>(null)
    return (
      <div ref={divRef}>
        <Editor
          apiKey={apiKey}
          onInit={(evt, editor) => editorRef.current = editor}
          initialValue={initialValue}
          init={{
            height: height,
            menubar: menubar,
            plugins: plugins,
            toolbar: toolbar,
            content_style: content_style,
            ai_request: (request: any, respondWith:any ) => respondWith.string(() => Promise.reject("See docs to implement AI Assistant"))
          }}
          onEditorChange={(value,editor) => Streamlit.setComponentValue(value)}
          disabled={disabled}
        />
      </div>
    );
  }


export default withStreamlitConnection(App);
