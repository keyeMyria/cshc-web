import React from 'react';
import PropTypes from 'prop-types';
import uniqBy from 'lodash/uniqBy';
import { FilterName, NoFilter } from 'util/constants';
import {
  FilterGroup,
  BooleanFilter,
  TextFilter,
  OptionListFilter,
  SelectFilter,
} from 'components/filters';

const VenueFilterSet = ({ currentSeason, teams, divisions }) => {
  const teamOptions = teams.map(team => ({ value: team.slug, label: team.long_name }));
  const divisionOptions = uniqBy(divisions, 'id').map(division => ({
    value: division.id,
    label: division.name,
  }));

  teamOptions.unshift({ value: NoFilter, label: 'All' });
  return (
    <div>
      <TextFilter filterName={FilterName.TextSearch} />
      <BooleanFilter filterName={FilterName.HomeGround} label="Home Grounds only" />
      <BooleanFilter
        filterName={FilterName.Season}
        label="Current Season only"
        trueValue={currentSeason}
      />
      <FilterGroup title="Team">
        <OptionListFilter filterName={FilterName.Team} options={teamOptions} />
      </FilterGroup>
      <FilterGroup title="Division">
        <SelectFilter
          filterName={FilterName.Division}
          options={divisionOptions}
          placeholder="Select a division..."
          openUpwards
        />
      </FilterGroup>
    </div>
  );
};

VenueFilterSet.propTypes = {
  currentSeason: PropTypes.string.isRequired,
  teams: PropTypes.arrayOf(
    PropTypes.shape({
      slug: PropTypes.string,
      long_name: PropTypes.string,
    }),
  ).isRequired,
  divisions: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number,
      name: PropTypes.string,
    }),
  ).isRequired,
};

VenueFilterSet.defaultProps = {};

export default VenueFilterSet;
