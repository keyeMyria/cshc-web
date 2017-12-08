import gql from 'graphql-tag';
import { compose, graphql } from 'react-apollo';
import withApolloResults from 'components/common/ApolloResults';

export const COMMITTEE_MEMBERSHIPS_QUERY = gql`
  query CommitteeMemberships($memberId: ID!) {
    committeeMemberships(member_Id: $memberId) {
      edges {
        node {
          season {
            slug
          }
          position {
            name
          }
        }
      }
    }
  }
`;

export const committeeMembershipsOptions = {
  options: ({ memberId }) => ({
    variables: {
      memberId,
    },
    fetchPolicy: 'cache-and-network',
  }),
  props: ({ ownProps, data: { networkStatus, error, committeeMemberships }, ...props }) => ({
    networkStatus,
    error,
    data: committeeMemberships,
    ...props,
  }),
};

export default compose(
  graphql(COMMITTEE_MEMBERSHIPS_QUERY, committeeMembershipsOptions),
  withApolloResults,
);