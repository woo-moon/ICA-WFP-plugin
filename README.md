<p>Make ICA maps</p>
        <p>This plugin is for spatial analysis in ICA reports required by WFP.</p>
        Download it to the folder "C:\Users\users_name\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins" (the folder you install your QGIS)
        <p>In module "Set Administration Layer and CRS", click the button "set Admin Shapefile and CRS". In the popping up window, select the shapefile of the country on the proper administrative level (usually the second level), and the CRS will be identified automatically. </p>
        <p>In the module "Rapid Shock Analysis", double click the items in the list. In the popping up window, select the raster layer for the concerning shock. For functions, select the statistical methods (percentage and mean are recommended by WFP). for the Palette, you may want to use the pre-defined Palette, or define a new palette for Class Low, Medium and High. <p>
        <p>In the module "Slow Shock Analysis", double click the items in the list. In the popping up window, select the raster layer for the concerning shock. Set a threshold the years with the concerning shock above which is identified as a shock-threatened year. Use a pre-defined palette or a new palette. <p>
        <p>If the shock you are concerning about is not listed above, click "Add Shock" to activate a new name of shock.<p>
        <p>In the module "LULC Analysis", click the button to activate the window for input data. Select raster layers of land use and land cover (usually more than one year) downloaded from LAADS in base year (like 2001-2003) and recent years (like 2020-2022)here. You can see the land degradation during this period. <p>
        <p>Now you can check all the attributes in the list "Attributes for Analysis". If you want to remove one attribute, select it in the list, and click "Remove". <p>
        <p>By clicking "Add Layers", you can set the shapefile for Food Security, another attribute for ICA besides natural shocks. In the popping window, select the shapefile of the Food Security. The names of all columns are loaded into the box of Select Column. Select the column for analysis. Please be sure the shapefile are prepared with Low, Medium and High classes. <p>
        <p>In the Output Folder, select a folder to reserve all the results, since there will be many. You can also check all the outputs in this folder. <p>
        <p>Click "Run Analysis" to see all the results, or Click "Reload" button to clear all the element for a new project. <p>
        
