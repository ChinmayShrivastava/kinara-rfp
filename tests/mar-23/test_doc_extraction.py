import pytest
from rfpextractor.scripts import DocExtraction

def test_DocExtraction_init():
    doc_ext = DocExtraction('testpdf.pdf', verbose=True)
    assert doc_ext.pdf_path == 'testpdf.pdf'
    assert doc_ext.verbose == True

def test_DocExtraction_run(mocker):
    mocker.patch.object(DocExtraction, '_run_extraction_pipeline')
    doc_ext = DocExtraction('testpdf.pdf')
    doc_ext.run()
    doc_ext._run_extraction_pipeline.assert_called_once()

def test_DocExtraction_run_extraction_pipeline(mocker):
    # Mock the state_manager attribute itself
    mock_state_manager = mocker.MagicMock()
    mocker.patch.object(DocExtraction, 'state_manager', new=mock_state_manager)
    
    # Now that state_manager is mocked, you can set up get_current_state and complete_state on the mock
    mocker.patch.object(DocExtraction, 'callbacks')
    
    doc_ext = DocExtraction('testpdf.pdf')
    doc_ext._run_extraction_pipeline()
    
    # Use the mock_state_manager to assert the calls
    mock_state_manager.get_current_state.assert_called_once()
    doc_ext.callbacks.assert_called_once()
    mock_state_manager.complete_state.assert_called_once()