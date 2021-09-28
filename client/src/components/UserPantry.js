import React, { useState } from "react";
import { Row, Col, ListGroup } from "react-bootstrap";
import IngredientCard from "./cards/IngredientCard";
import axios from "axios";

import { usePantryContext } from "../context/PantryContext";
import { useRecipesContext } from "../context/RecipesContext";

const CONFIG = {
  headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*"
  }
};

const url = "http://api.cs.brown.edu:3000";

export default function UserPantry() {
  const searchRecipes = async (pantry, setRecipes) => {
    let ingredients = [...pantry].join(",");
    let res = await axios.get(`${url}/?ing[]=${ingredients}`, CONFIG);
    setRecipes(res.data);
  };

  // pantry is an array of objects representing an ingredient
  // render an ingredient card for every pantry item in the pantry list
  const { pantry, setPantry } = usePantryContext();

  // remove duplicate ingredients
  const ingrSet = new Set();
  const p = pantry.filter(ingr => {
    const b = !ingrSet.has(ingr.label);
    ingrSet.add(ingr.label);
    return b;
  });

  // send ingredients to server and update recipes list
  const { recipes, setRecipes } = useRecipesContext();

  searchRecipes(ingrSet, setRecipes);

  // turn ingredients into element list
  const ingrList = p.map(ingr => {
    return (
      <ListGroup.Item>
        <IngredientCard name={ingr.label} />
      </ListGroup.Item>
    );
  });

  return (
    <div className="mt-4">
      <ListGroup variant="flush" id="pantry-list">
        {ingrList}
      </ListGroup>
    </div>
  );
}
