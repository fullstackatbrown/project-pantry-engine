import React from "react";
import {
  Card,
  Row,
  Col,
  Image,
  ListGroup,
  Modal,
  Button
} from "react-bootstrap";

import { UsePantryContext } from "../../context/PantryContext.js";

const openInNewTab = url => {
  const newWindow = window.open(url, "_blank", "noopener,noreferrer");
  if (newWindow) newWindow.opener = null;
};

function RecipePreview(props) {
  return (
    <Modal
      {...props}
      size="lg"
      aria-labelledby="contained-modal-title-vcenter"
      centered
    >
      <Modal.Body>
        <Row>
          <Col>
            <Row>
              <Modal.Title id="recipe-preview-name">
                {props.recipeTitle}
              </Modal.Title>
            </Row>
            <Row>
              <Button onClick={() => openInNewTab(props.recipeUrl)}>
                See Recipe
              </Button>
            </Row>
          </Col>
          <Col>
            <Image
              className="recipe-preview-image"
              src={props.imgUrl}
              onClick={() => openInNewTab(props.recipeUrl)}
            />
          </Col>
        </Row>
        <Row className="recipe-preview-text">
          <h2>in my pantry</h2>
          <p>eggs, tomatoes, peppers, onions, jalapeños</p>
          <h2>i need</h2>
          <p className="ingredients-missing">paprika, sour cream, pita bread</p>
        </Row>
      </Modal.Body>
    </Modal>
  );
}

export default function RecipeCard(props) {
  const [modalShow, setModalShow] = React.useState(false);

  return (
    <>
      <Card className="recipe-card floating" onClick={() => setModalShow(true)}>
        <Card.Body className="p-0">
          <Row className="m-0">
            <Col xs={5} className="m-0 p-2">
              <Image className="recipe-card-image" src={props.imgUrl} />
            </Col>
            <Col className="m-0 p-2">
              <Card.Title>{props.recipeTitle}</Card.Title>
              <ListGroup variant="flush">
                <ListGroup.Item className="ingredients-possessed">
                  eggs, tomatoes, peppers, onions, anchovies
                </ListGroup.Item>
                <ListGroup.Item className="ingredients-missing">
                  paprika, sour cream, pineapple
                </ListGroup.Item>
              </ListGroup>
            </Col>
          </Row>
        </Card.Body>
      </Card>

      <RecipePreview
        className="recipe-preview"
        show={modalShow}
        onHide={() => setModalShow(false)}
        recipeTitle={props.recipeTitle}
        recipeUrl={props.recipeUrl}
        imgUrl={props.imgUrl}
      />
    </>
  );
}
