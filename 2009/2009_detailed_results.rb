require 'tabula'

pdf_file_path = "2009_detailed_results.pdf"
outfilename = "raw_data_2009_constituency.csv"

out = open(outfilename, 'w')

extractor = Tabula::Extraction::ObjectExtractor.new(pdf_file_path, 1..197)
extractor.extract.each_with_index do |pdf_page, page_index|
  page_areas = [[100, 0, 900, 1700]]

  scale_factor = pdf_page.width / 1700 
  # where 1700 is the width of the page as you measured it.

  vertical_ruling_locations = [0, 470,640, 906,1080, 1200, 1400, 1548] #column locations
  vertical_rulings = vertical_ruling_locations.map{|n| Tabula::Ruling.new(0, n * scale_factor, 0, 1000)}

  page_areas.each do |page_area|
    out << pdf_page.get_area(page_area).get_table(:vertical_rulings => vertical_rulings).to_csv
    out << "\n\n"
  end
end
extractor.close!
out.close