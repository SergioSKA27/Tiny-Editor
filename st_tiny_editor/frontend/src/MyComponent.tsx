import {
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode, useEffect, useState  } from "react"
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
