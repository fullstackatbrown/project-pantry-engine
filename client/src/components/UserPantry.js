import React, { useState } from 'react'
import { Row, Col, ListGroup } from 'react-bootstrap'
import IngredientCard from './cards/IngredientCard'
import axios from 'axios'

import { usePantryContext } from '../context/PantryContext'

// PLACEHOLDER
const url = "http://localhost:4000/"

// TODO: get all items in pantry and run search request
export default function UserPantry() {
  // TODO: finish this

  const searchRecipes = () => {
    axios.post(url, {
      test: "test"
    })
      .then((data) => {
        setPantry(data)
      }).catch((error) => console.log(error))
  }

  // pantry is an array of objects representing an ingredient

  // render an ingredient card for every pantry item in the pantry list

  const { pantry, setPantry } = usePantryContext()

  const ingrList = pantry.map((ingr) => {
    return <ListGroup.Item> <IngredientCard name={ingr.name} /> </ListGroup.Item>
  })

  return (
    <div className="mt-4">
      <ListGroup variant="flush" id="pantry-list">
        {ingrList}

        <ListGroup.Item> <IngredientCard name="onion"/> </ListGroup.Item>
        <ListGroup.Item> <IngredientCard name="onion2"/> </ListGroup.Item>

      </ListGroup>

    </div>
  )
}
