import react from 'react';
import { Fab } from '@material-ui/core';

const Pilot_button = () => {
  const styles = {
        margin: 'auto'
      
    }

    const handleClick = () => {
      window.location.href = './pages/pilot_home';
    }

    return(
        <div style = {styles}>
            <Fab variant="extended" onClick={() => handleClick()}
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
