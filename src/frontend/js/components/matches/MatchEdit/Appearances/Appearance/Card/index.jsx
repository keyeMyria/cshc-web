import React from 'react';
import PropTypes from 'prop-types';
import classnames from 'classnames';
import Urls from 'util/urls';
import styles from './style.scss';

const AppearanceCard = ({ color, imagePath, isSelected, onClick }) => (
  <div
    className={classnames(styles.cardButton, { [styles.notSelected]: !isSelected })}
    role="button"
    tabIndex="0"
    title={`${color} Card`}
    onClick={onClick}
  >
    <img className="g-px-10" alt={`${color} Card`} src={Urls.static(imagePath)} />
  </div>
);

AppearanceCard.propTypes = {
  color: PropTypes.oneOf(['Green', 'Yellow', 'Red']).isRequired,
  imagePath: PropTypes.string.isRequired,
  isSelected: PropTypes.bool.isRequired,
  onClick: PropTypes.func.isRequired,
};

export default AppearanceCard;
