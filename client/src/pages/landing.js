import react from 'react';
import Pilot_button from "../components/buttons/pilot_button";
import ATC_button from "../components/buttons/atc_button";

import { Fab } from '@material-ui/core';

const Landing = () => {
  const styles = {
    display: 'flex',
    flexDirection: 'column',
    marginTop: '20vh',
    alignItems: 'center'
  }
  return (
      <div style = {styles}>
      <h1> What is your role? </h1>
      <Pilot_button/>
      <ATC_button/>
      </div>
  )
};

export default Landing
