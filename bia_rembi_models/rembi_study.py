from typing import List, Optional
from pydantic import BaseModel
from .study import Study
from .study_component import StudyComponent
from .sample import Biosample
from .specimen import Specimen
from .acquisition import ImageAcquisition
from .analysis import ImageAnalysis
from .correlation import ImageCorrelation
from bia_mifa_models.pydantic_model import Annotations

class REMBIStudy(BaseModel):
    study: Study
    study_components: List[StudyComponent]
    sample: List[Biosample]
    specimen: List[Specimen]
    image_acquisition: List[ImageAcquisition]
    image_correlation: Optional[ImageCorrelation] = None
    image_analysis: Optional[ImageAnalysis] = None
    annotations: Optional[Annotations] = None
