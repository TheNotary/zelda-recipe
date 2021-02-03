
import React, {useEffect} from "react";

import { NavLink } from "react-router-dom";
import { connect } from "react-redux";
import propTypes from "prop-types";
// import { bindActionCreators } from "redux";

const Header = ({currentUserName, actions, ...props}) => {
  const activeStyle = { color: "#F15B2A" };


  useEffect(() => {
    console.log("I used header effects");
  });

  return (
    <nav>
      <NavLink to="/" activeStyle={activeStyle} exact>
        Home
      </NavLink>
      {" | "}
      <NavLink to="/about" activeStyle={activeStyle}>
        About
      </NavLink>
    </nav>
  );
};

Header.propTypes = {
  actions: propTypes.object.isRequired,
};

// Redux will magically call this when our state.users object changes following
// an action being sent to a reducer modifieing state.users
function mapStateToProps(state) {
  return {
    // currentUserName: state.login.currentUserName,
  };
}

// this fancy method gets installed into the components props for you per the export line below
function mapDispatchToProps(dispatch) {
  return {
    actions: {
      // setCurrentUsername: bindActionCreators(loginSliceActions.setCurrentUsername, dispatch),
      // logout: bindActionCreators(loginSliceActions.logout, dispatch),
    },
  };
}

// export default UsersPage;
export default connect(mapStateToProps, mapDispatchToProps)(Header);
