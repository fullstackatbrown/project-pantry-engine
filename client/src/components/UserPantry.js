import React, { useState } from 'react'
import { Row, Col, ListGroup } from 'react-bootstrap'
import IngredientCard from './cards/IngredientCard'
import axios from 'axios'

// PLACEHOLDER
const url = "insert server url here"

// const searchRecipes = () => {
//     axios.post(url, { 
//         test: "test"
//     })
//     .then((data) => {
//         console.log(data)
//     }).catch((error) => console.log(error))
// }

// TODO: get all items in pantry and run search request
export default function UserPantry() {
    // TODO: finish this

    // pantry is an array of objects representing an ingredient
    // TODO: --------- useContext() instead ??? ----------
    const [pantry, setPantry] = useState([])

    // render an ingredient card for every pantry item in the pantry list
    return (
        <div className="mt-4">
            <ListGroup variant="flush" id="pantry-list"> 
                <ListGroup.Item> <IngredientCard/> </ListGroup.Item>
                <ListGroup.Item> <IngredientCard/> </ListGroup.Item>
                <ListGroup.Item> <IngredientCard/> </ListGroup.Item>
                <ListGroup.Item> <IngredientCard/> </ListGroup.Item>
                <ListGroup.Item> <IngredientCard/> </ListGroup.Item>
                <ListGroup.Item> <IngredientCard/> </ListGroup.Item>
                <ListGroup.Item> <IngredientCard/> </ListGroup.Item>
                <ListGroup.Item> <IngredientCard/> </ListGroup.Item>
                <ListGroup.Item> <IngredientCard/> </ListGroup.Item>
                <ListGroup.Item> <IngredientCard/> </ListGroup.Item>

            </ListGroup> 
            
        </div>
    )
}
