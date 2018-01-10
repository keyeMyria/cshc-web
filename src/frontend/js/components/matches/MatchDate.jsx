import React from 'react';
import PropTypes from 'prop-types';
import { format as dateFormat } from 'date-fns';
import Urls from 'util/urls';

/** Represention of a match date. Includes a hyperlink to display all matches on that date.
 */
const MatchDate = ({ date, format }) => {
  const formattedDate = dateFormat(date, format);
  const formattedLinkDate = dateFormat(date, 'DD-MM-YYYY');
  return (
    <a title={`Matches on ${formattedDate}`} href={Urls.matches_on_date(formattedLinkDate)}>
      {formattedDate}
    </a>
  );
};

MatchDate.propTypes = {
  date: PropTypes.string.isRequired,
  format: PropTypes.string,
};

MatchDate.defaultProps = {
  format: 'Do MMM',
};

export default MatchDate;
