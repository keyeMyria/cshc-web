import React from 'react';
import PropTypes from 'prop-types';

/**
 * Loading/spinner component - typically displayed while fetching GraphQL data using Apollo.
 */
const Loading = ({ message }) => (
  <div className="g-mb-20 g-mt-20 g-flex-centered">
    <div className="g-flex-centered-item g-text-center">
      <i className="fas fa-spinner fa-spin" />
      {message && <span className="g-ml-5">{message}</span>}
    </div>
  </div>
);

Loading.propTypes = {
  message: PropTypes.string,
};

Loading.defaultProps = {
  message: undefined,
};

module.exports = Loading;
