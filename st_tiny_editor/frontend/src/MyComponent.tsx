import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode,useRef } from "react"
import { Editor } from '@tinymce/tinymce-react';
import App from "./tiny";




interface State {
  args: any
}

class TinyEditor extends StreamlitComponentBase<State>{
  public state = { args: {} }
  public render = (): ReactNode => {

    return (
    <>
      <App/>
    </>);


}
}

export default withStreamlitConnection(TinyEditor);
