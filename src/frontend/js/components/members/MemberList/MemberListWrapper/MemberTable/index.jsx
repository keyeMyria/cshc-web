import React from 'react';
import PropTypes from 'prop-types';
import MemberTableRow from './MemberTableRow';

const MemberTable = ({ members }) => (
  <div className="table-responsive">
    <table className="table table-sm table-hover">
      <thead>
        <tr>
          <th>First Name</th>
          <th>Last Name</th>
          <th className="priority3">
            <abbr title="Male/Female">M/F</abbr>
          </th>
          <th className="priority3">Position</th>
          <th className="priority3">Shirt #</th>
          <th>Appearances</th>
          <th>Goals</th>
        </tr>
      </thead>
      <tbody>
        {members.edges.map(member => <MemberTableRow key={member.node.id} member={member.node} />)}
      </tbody>
    </table>
  </div>
);

MemberTable.propTypes = {
  members: PropTypes.shape().isRequired,
};

export default MemberTable;