import React, { Component } from 'react';
import { Card, Row, Col, Image, ListGroup } from 'react-bootstrap';

class RecipeCard extends Component {
    render() {
        return (
            <Card className="recipe-card floating">
                <Card.Body className="p-0">
                    <Row className="m-0">
                        <Col xs={5} className="m-0 p-2">
                            <Image className="recipe-card-image" src="https://images.immediate.co.uk/production/volatile/sites/30/2020/08/chorizo-mozarella-gnocchi-bake-cropped-9ab73a3.jpg?quality=90&resize=960,872" />
                        </Col>
                        <Col className="m-0 p-2">
                            <Card.Title>recipe name</Card.Title>
                            <ListGroup variant="flush">
                                <ListGroup.Item className="ingredients-possessed">eggs, tomatoes, peppers, onions, anchovies</ListGroup.Item>
                                <ListGroup.Item className="ingredients-missing">paprika, sour cream, pineapple</ListGroup.Item>
                            </ListGroup>
                        </Col>
                    </Row>
                </Card.Body>
            </Card>
        );
    }
}

export default RecipeCard;