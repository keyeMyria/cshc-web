import React from 'react';
import PropTypes from 'prop-types';
import Select from 'react-select';
import CKEditor from 'react-ckeditor-component';
import CkEditorConfig from 'util/CkEditorConfig';
import { SelectValueLabelOptionsPropType } from 'components/common/PropTypes';
import { toSelectOption } from '../util';

export const ReportPropType = PropTypes.shape({
  author: PropTypes.string,
  title: PropTypes.string,
  content: PropTypes.string,
});

/**
 * The 4th and final step of the Match Editing form.
 * 
 * A fairly simple form for entering the report author (must be a member),
 * the report title and the report content (using a CKEditor editor).
 */
class Report extends React.Component {
  constructor(props) {
    super(props);
    const parser = new DOMParser();
    const dom = parser.parseFromString(`<!doctype html><body>${props.report.content}`, 'text/html');
    const decodedReportContent = dom.body.innerHTML.replace(/\\r\\n/g, ' ');

    this.state = {
      title: props.report.title || '',
      content: decodedReportContent || '',
    };
    this.onBlurContent = this.onBlurContent.bind(this);
    this.updateAuthor = this.updateAuthor.bind(this);
    this.updateTitle = this.updateTitle.bind(this);
    this.updateContent = this.updateContent.bind(this);
  }

  onBlurContent() {
    this.props.onUpdateReport({
      ...this.props.report,
      content: this.state.content,
    });
  }

  updateAuthor(value) {
    this.props.onUpdateReport({
      ...this.props.report,
      author: value,
    });
  }

  updateTitle(ev) {
    this.setState({ title: ev.target.value });
    this.props.onUpdateReport({
      ...this.props.report,
      title: ev.target.value,
    });
  }

  updateContent(ev) {
    const newContent = ev.editor.getData();
    this.setState({ content: newContent });
  }

  render() {
    const { authorOptions, report } = this.props;
    const { content, title } = this.state;
    return (
      <div className="card-block">
        <div className="form-group g-mb-20">
          <label htmlFor="report-author">Author</label>
          <Select
            id="report-author"
            className="g-max-width-400--md"
            placeholder="Select author..."
            options={authorOptions}
            simpleValue
            clearable
            searchable
            name="report-author-select"
            value={toSelectOption(report.author)}
            onChange={this.updateAuthor}
          />
        </div>
        <div className="form-group g-mb-20">
          <label htmlFor="report-title">Title</label>
          <input
            id="report-title"
            className="form-control form-control-md rounded-0 g-max-width-400--md"
            type="text"
            value={title}
            onChange={this.updateTitle}
          />
        </div>
        <div className="form-group g-mb-20">
          <label htmlFor="report-content">Match Report</label>
          <CKEditor
            activeClass=""
            config={CkEditorConfig}
            isScriptLoaded
            content={content}
            events={{ change: this.updateContent, blur: this.onBlurContent }}
          />
        </div>
      </div>
    );
  }
}

Report.propTypes = {
  authorOptions: SelectValueLabelOptionsPropType.isRequired,
  report: ReportPropType.isRequired,
  onUpdateReport: PropTypes.func.isRequired,
};

Report.defaultProps = {};

export default Report;
