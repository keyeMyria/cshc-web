import React from 'react';
import PropTypes from 'prop-types';
import VenueTableRow from './VenueTableRow';

const VenueTable = ({ venues }) => (
  <div className="table-responsive">
    <table className="table table-sm table-hover">
      <thead>
        <tr>
          <th>Venue</th>
          <th>Address</th>
          <th>
            <abbr title="Distance in miles from Cambridge">Distance</abbr>
          </th>
        </tr>
      </thead>
      <tbody>{venues.map(venue => <VenueTableRow key={venue.id} venue={venue} />)}</tbody>
    </table>
  </div>
);

VenueTable.propTypes = {
  venues: PropTypes.shape().isRequired,
};

export default VenueTable;
