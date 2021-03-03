import react from 'react';
import { Fab } from '@material-ui/core';

const Pilot_button = () => {
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
                Pilot
            </Fab>
        </div>
    )
}

export default Pilot_button;
