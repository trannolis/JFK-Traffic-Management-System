import react from 'react';
import { Fab } from '@material-ui/core';

const ATC_button = () => {
  const styles = {
        margin: 'auto'
    }
    return(
        <div style = {styles}>
            <Fab variant="extended"
            classes={{
                        root: 'muiFab',
                        label: 'muiFabLabel'
                    }}>
                Air Traffic Controller
            </Fab>
        </div>
    )
}

export default ATC_button;
