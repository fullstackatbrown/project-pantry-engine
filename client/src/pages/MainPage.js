import React from 'react'
import { Container, Row } from 'react-bootstrap'
import UserIngredientBlock from '../components/UserIngredientBlock'
import RecipeBlock from '../components/RecipeBlock'

export default function MainPage() {
    return (
        <Container className="mt-1 mx-5" fluid="xl">
            <Row>
                <UserIngredientBlock />
                <RecipeBlock />
            </Row>
        </Container>
    )
}