import React from 'react';
import PropTypes from 'prop-types';
import { NetworkStatus as NS } from 'apollo-client';
import ErrorDisplay from 'components/common/ErrorDisplay';
import Loading from 'components/common/Loading';

const LeagueTable = ({ networkStatus, error, divisionResults }) => {
  if (networkStatus === NS.loading) return <Loading message="Fetching league table..." />;
  if (error) return <ErrorDisplay errorMessage="Failed to load league table" />;
  return (
    <table className="table table-sm table-hover table-responsive">
      <thead>
        <tr>
          <th>Team</th>
          <th>
            <abbr title="Played">P</abbr>
          </th>
          <th>
            <abbr title="Won">W</abbr>
          </th>
          <th>
            <abbr title="Drawn">D</abbr>
          </th>
          <th>
            <abbr title="Lost">L</abbr>
          </th>
          <th>
            <abbr title="Goals For">GF</abbr>
          </th>
          <th>
            <abbr title="Goals Against">GA</abbr>
          </th>
          <th>
            <abbr title="Goal Difference">GD</abbr>
          </th>
          <th>
            <abbr title="Points">Pts</abbr>
          </th>
          <th>&nbsp;</th>
        </tr>
      </thead>
      <tbody>
        {divisionResults.edges.map((rowEdge) => {
          const row = rowEdge.node;
          const rowClass = row.ourTeam ? 'table-success' : '';
          return (
            <tr key={row.teamName} className={rowClass}>
              <td>
                <a href="#">{row.teamName}</a>
              </td>
              <td>{row.played}</td>
              <td>{row.won}</td>
              <td>{row.drawn}</td>
              <td>{row.lost}</td>
              <td>{row.goalsFor}</td>
              <td>{row.goalsAgainst}</td>
              <td>{row.goalDifference}</td>
              <td>{row.points}</td>
              <td>{row.notes}</td>
            </tr>
          );
        })}
      </tbody>
    </table>
  );
};

LeagueTable.propTypes = {
  networkStatus: PropTypes.number.isRequired,
  error: PropTypes.instanceOf(Error),
  divisionResults: PropTypes.shape(),
};

LeagueTable.defaultProps = {
  error: undefined,
  divisionResults: undefined,
};

export default LeagueTable;