import { isPast } from 'date-fns';
import sortBy from 'lodash/sortBy';
import reduce from 'lodash/reduce';
import { toTitleCase } from 'util/cshc';
import { HomeAway, MatchAward } from 'util/constants';

/**
 * Utility object for common logic related to a match.
 */
const Match = {
  isHome(match) {
    return match.homeAway === HomeAway.Home;
  },

  isPast(match) {
    return isPast(`${match.date} ${match.time}`);
  },

  datetime(match) {
    if (!match) return undefined;
    return new Date(`${match.date} ${match.time}`);
  },

  simpleVenueName(match) {
    if (match.venue) {
      if (Match.isHome(match)) {
        return match.venue.shortName || match.venue.name;
      }
      return 'Away';
    } else if (Match.isPast(match)) return '???';
    return 'TBD';
  },

  finalScoresProvided(match) {
    return (
      (match.ourScore === 0 || match.ourScore > 0) && (match.oppScore === 0 || match.oppScore > 0)
    );
  },

  scoreDisplay(match) {
    if (match.altOutcome) {
      return toTitleCase(match.altOutcome);
    }
    if (!Match.finalScoresProvided(match)) {
      return '-';
    }
    return `${match.ourScore}-${match.oppScore}`;
  },

  resultClass(match) {
    if (match.altOutcome || !Match.finalScoresProvided(match)) return '';
    if (match.ourScore > match.oppScore) return 'g-bg-green g-color-white';
    else if (match.ourScore < match.oppScore) return 'g-bg-red g-color-white';
    return 'g-bg-black-opacity-0_3 g-color-white';
  },

  scorers(match) {
    if (!match.appearances) return [];
    return sortBy(match.appearances.filter(a => a.goals > 0), m => -m.goals);
  },

  mom(match) {
    if (!match.awardWinners) return [];
    return match.awardWinners.filter(aw => aw.award.name === MatchAward.MOM);
  },

  lom(match) {
    if (!match.awardWinners) return [];
    return match.awardWinners.filter(aw => aw.award.name === MatchAward.LOM);
  },

  toResultsAndFixtures(matches) {
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
    return matchStructure;
  },
};

export default Match;
