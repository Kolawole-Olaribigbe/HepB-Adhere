import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
const Router: any = BrowserRouter;
import Dashboard from './components/Dashboard';

const App: React.FC = () => {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Dashboard} />
        {/* Additional routes can be added here */}
      </Switch>
    </Router>
  );
};

export default App;