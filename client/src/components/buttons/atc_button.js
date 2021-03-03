import react from 'react';
import { Fab } from '@material-ui/core';

const ATC_button = () => {
  const styles = {
        margin: 'auto'

    }

  const handleClick = () => {
    window.location.href = './pages/atc_home';
  }
    return(
        <div style = {styles}>
            <Fab variant="extended" onClick={() => handleClick()}
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
