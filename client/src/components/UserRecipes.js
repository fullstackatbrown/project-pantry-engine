import React, { useState } from "react";
import { Row, Col, ListGroup } from "react-bootstrap";
import RecipeCard from "./cards/RecipeCard";

import { useRecipesContext } from "../context/RecipesContext";

export default function UserRecipes() {
  const recipes = [1, 2, 3];
  const recipesList = recipes.map(r => {
    return (
      <ListGroup.Item>
        <RecipeCard
          recipeTitle="How To Make The Fluffiest Pancakes"
          recipeUrl="https://tasty.co/recipe/tasty-101-buttermilk-pancakes"
          imgUrl="https://img.buzzfeed.com/thumbnailer-prod-us-east-1/video-api/assets/167797.jpg"
        />
      </ListGroup.Item>
    );
  });

  return (
    <div className="mt-4">
      <ListGroup variant="flush">
        {recipesList}
      </ListGroup>
    </div>
  );
}
