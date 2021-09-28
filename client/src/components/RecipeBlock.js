import React, { Component } from "react";
import { Row, Col } from "react-bootstrap";
import SearchBarRecipe from "./search_bars/SearchBarRecipe.js";
import UserRecipes from "./UserRecipes.js";
import RecipeCard from "./cards/RecipeCard.js";

class RecipeBlock extends Component {
  render() {
    return (
      <Col>
        <SearchBarRecipe />
        <UserRecipes />
      </Col>
    );
  }
}

export default RecipeBlock;
