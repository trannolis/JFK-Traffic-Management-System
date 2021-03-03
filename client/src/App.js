import './App.css';
import {
  BrowserRouter as Router,
  withRouter,
  Switch,
  Route,
  Link
} from "react-router-dom";

import Landing from './pages/landing';
import HomeATC from './pages/atc_home';
import HomePilot from './pages/pilot_home';


export default function App() {
  return (
     <Router>
       <div>
         {/* A <Switch> looks through its children <Route>s and
             renders the first one that matches the current URL. */}
         <Switch>
           <Route path="/pages/atc_home">
            <HomeATC/>
            </Route>
           <Route path ="/pages/pilot_home">
            <HomePilot/>
          </Route>
          <Route path="/">
            <Landing/>
          </Route>
         </Switch>
       </div>
     </Router>
   );
 }
