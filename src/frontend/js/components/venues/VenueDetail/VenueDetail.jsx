import React from 'react';
import PropTypes from 'prop-types';
import reduce from 'lodash/reduce';
import sortBy from 'lodash/sortBy';
import { NetworkStatus as NS } from 'apollo-client';
import { MatchItem } from 'util/constants';
import ErrorDisplay from 'components/common/ErrorDisplay';
import Loading from 'components/common/Loading';
import MatchList from 'components/matches/MatchList';
import Match from 'models/match';
import Accordion from 'components/common/Accordion';
import AccordionCard from 'components/common/Accordion/AccordionCard';

/**
 * Wrapper component for components relating to a particular venue.
 * 
 * Includes:
 * - Previous results at this venue (organised by our team)
 * - Upcoming fixtures at this venue (organised by our team)
 */
const VenueDetail = ({ networkStatus, error, matches, venueName }) => {
  if (networkStatus === NS.loading) return <Loading message="Loading matches..." />;
  if (error) return <ErrorDisplay errorMessage="Failed to load matches" />;

  const matchStructure = {
    results: [],
    fixtures: [],
  };
  // Sort by past results vs future fixtures and by team
  reduce(
    matches.edges,
    (acc, matchEdge) => {
      const list = Match.isPast(matchEdge.node) ? acc.results : acc.fixtures;
      let teamMatches = list.find(md => md.team.id === matchEdge.node.ourTeam.id);
      if (!teamMatches) {
        teamMatches = { team: matchEdge.node.ourTeam, matches: [] };
        list.push(teamMatches);
      }
      teamMatches.matches.push(matchEdge.node);
      return acc;
    },
    matchStructure,
  );
  // Sort by team position
  matchStructure.results = sortBy(matchStructure.results, ['team.position']);
  matchStructure.fixtures = sortBy(matchStructure.fixtures, ['team.position']);

  return (
    <div>
      <div className="u-heading-v1-6 g-bg-main g-brd-gray-light-v2 g-mb-20 g-mt-20">
        <h2 className="h3 u-heading-v1__title">Past results at {venueName}</h2>
      </div>
      {matchStructure.results.length > 0 ? (
        <Accordion accordionId="results">
          {matchStructure.results.map(m => (
            <AccordionCard
              key={m.team.id}
              cardId={m.team.id}
              accordionId="results"
              title={m.team.longName}
            >
              <MatchList matches={m.matches} exclude={['venue']} dateFormat="Do MMM YY" />
            </AccordionCard>
          ))}
        </Accordion>
      ) : (
        <p className="lead">No previous matches at this venue</p>
      )}
      <div className="u-heading-v1-6 g-bg-main g-brd-gray-light-v2 g-mb-20 g-mt-20">
        <h2 className="h3 u-heading-v1__title">Upcoming fixtures at {venueName}</h2>
      </div>
      {matchStructure.fixtures.length > 0 ? 
      <Accordion accordionId="fixtures">
        {matchStructure.fixtures.map(m => (
          <AccordionCard
            key={m.team.id}
            cardId={m.team.id}
            accordionId="fixtures"
            title={m.team.longName}
          >
            <MatchList
              matches={m.matches}
              exclude={[MatchItem.venue, MatchItem.result, MatchItem.scorers, MatchItem.awards]}
            />
          </AccordionCard>
        ))}
      </Accordion>
      ) : (
        <p className="lead">No upcoming fixtures at this venue</p>
      )}
    </div>
  );
};

VenueDetail.propTypes = {
  venueName: PropTypes.string.isRequired,
  networkStatus: PropTypes.number.isRequired,
  error: PropTypes.instanceOf(Error),
  matches: PropTypes.shape(),
};

VenueDetail.defaultProps = {
  error: undefined,
  matches: undefined,
};

export default VenueDetail;
