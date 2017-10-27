import React from 'react';
import PropTypes from 'prop-types';
import { format } from 'date-fns';
import Match from 'models/match';
import MemberLink from 'components/members/MemberLink';
import AwardWinner from 'components/awards/AwardWinner';
import { MatchItem as TC } from 'util/constants';
import FixtureTypeIcon from '../../FixtureTypeIcon';
import MatchDate from '../../MatchDate';
import OppositionTeam from '../../OppositionTeam';
import KitClash from '../../KitClash';
import MatchVenue from '../../MatchVenue';
import MatchLink from '../../MatchLink';
import styles from './style.scss';

/**
 * Represents a single row in a table of matches.
 */
const MatchTableRow = ({ match, excludeColumns, priorities, dateFormat }) => {
  const incl = columnName => !excludeColumns.includes(columnName);
  const priority = (columnName, defaultPriority = 1) =>
    `align-middle priority${priorities[columnName] || defaultPriority}`;
  return (
    <tr>
      {incl(TC.fixtureType) && (
        <td className={priority(TC.fixtureType, 3)}>
          <FixtureTypeIcon fixtureType={match.fixtureType} />
        </td>
      )}
      {incl(TC.date) && (
        <td className={`${priority(TC.date)} no-break`}>
          <MatchDate date={match.date} format={dateFormat} />
        </td>
      )}
      {incl(TC.opposition) && (
        <td className={priority(TC.opposition)}>
          <OppositionTeam team={match.oppTeam} />
          <KitClash match={match} />
        </td>
      )}
      {incl(TC.time) && (
        <td className={priority(TC.time, 2)}>
          {match.time && format(Match.datetime(match), 'H:mm')}
        </td>
      )}
      {incl(TC.venue) && (
        <td className={priority(TC.venue, 2)}>
          <MatchVenue match={match} />
        </td>
      )}
      {incl(TC.result) && (
        <td className={`${priority(TC.result)} g-text-center`}>
          <span className={`${Match.resultClass(match)} g-py-5 g-px-8`}>
            {Match.scoreDisplay(match)}
          </span>
        </td>
      )}
      {incl(TC.scorers) && (
        <td className={priority(TC.scorers, 3)}>
          <div className={styles.flexWrap}>
            {Match.scorers(match).map(scorer => (
              <MemberLink
                key={scorer.member.modelId}
                member={scorer.member}
                badgeCount={scorer.goals}
                className="g-mr-10"
              />
            ))}
          </div>
        </td>
      )}
      {incl(TC.awards) && (
        <td className={priority(TC.awards, 3)}>
          <div className={styles.flexWrap}>
            {Match.mom(match).map((awardWinner, index) => (
              <AwardWinner key={index} awardWinner={awardWinner} className="g-mr-10" />
            ))}
          </div>
        </td>
      )}
      {incl(TC.awards) && (
        <td className={priority(TC.awards, 3)}>
          <div className={styles.flexWrap}>
            {Match.lom(match).map((awardWinner, index) => (
              <AwardWinner key={index} awardWinner={awardWinner} className="g-mr-10" />
            ))}
          </div>
        </td>
      )}
      {incl(TC.report) && (
        <td className={`${priority(TC.report)} g-text-center`}>
          <MatchLink match={match} />
        </td>
      )}
    </tr>
  );
};

MatchTableRow.propTypes = {
  match: PropTypes.shape().isRequired,
  excludeColumns: PropTypes.arrayOf(PropTypes.string),
  priorities: PropTypes.shape(),
  dateFormat: PropTypes.string,
};

MatchTableRow.defaultProps = {
  excludeColumns: [],
  priorities: {},
  dateFormat: 'Do MMM',
};

export default MatchTableRow;
