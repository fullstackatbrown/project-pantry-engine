import React from 'react'
import { Form, Row } from 'react-bootstrap'

export default function SearchBarIngredient() {
    return (
        <Form className="mt-4">
            <Form.Group as={Row}>
                <Form.Control className="ingredient-search-bar embedded rounded-pill mx-5" placeholder="search for ingredients"/> 
            </Form.Group>

        </Form>
    )
}
